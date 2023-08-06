# -*- coding: utf-8 -*-

__author__ = r'wsb310@gmail.com'

import sys
import time

from rich.table import Table
from rich.console import Console

from ..extend.interface import FunctorInterface, RunnableInterface

from ..extend.asyncio import command
from ..extend.asyncio.base import Utils, MultiTasks, AsyncCirculator
from ..extend.asyncio.zmq import Subscribe, PublishWithBuffer


SIGNAL_PROTOCOL = r'tcp'
SIGNAL_PORT = 83310
HIGH_WATER_MARK = 0xffffff


class TimerMS:

    __slots__ = [r'_timer']

    def __init__(self, timer=None):
        self._timer = time.time() if timer is None else timer

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.done()

    def done(self):
        self._timer = (time.time() - self._timer) * 1000

    @property
    def value(self):
        return self._timer


class Reporter(Subscribe):

    class _Report:

        def __init__(self):
            self.success = []
            self.failure = []

        def __len__(self):

            return len(self.success) + len(self.failure)

    def __init__(self):

        global SIGNAL_PROTOCOL, SIGNAL_PORT

        super().__init__(f'{SIGNAL_PROTOCOL}://*:{SIGNAL_PORT}', True)

        self._reports = {}

        self._timer = TimerMS()

    def __len__(self):

        return sum([len(item) for item in self._reports.values()])

    async def handle_message(self):

        while True:

            message = await self.recv(True)

            if message is None:
                break

            for name, result, resp_time in message:
                if name and result in (r'success', r'failure'):
                    getattr(self._get_report(name), result).append(resp_time)

    def _get_report(self, name: str) -> _Report:

        if name not in self._reports:
            self._reports[name] = self._Report()

        return self._reports[name]

    def open(self):

        global HIGH_WATER_MARK

        super().open(HIGH_WATER_MARK)

    def print_report(self):

        self._timer.done()

        headers = (
            r'EventName',
            r'SuccessTotal',
            r'FailureTotal',
            r'SuccessRatio',
            r'SuccessAveTime',
            r'SuccessMinTime',
            r'SuccessMaxTime',
        )

        _time = round(self._timer.value / 1000)
        _count = len(self)

        table = Table(
            *headers,
            title=f'Count: {_count}, Time: {_time}s, Qps: {round(_count / _time)}',
            show_lines=True
        )

        for key, val in self._reports.items():
            table.add_row(
                key,
                str(len(val.success)),
                str(len(val.failure)),
                r'{:.2%}'.format(len(val.success) / (len(val.success) + len(val.failure))),
                r'{:.3f}ms'.format(sum(val.success) / len(val.success) if len(val.success) > 0 else 0),
                r'{:.3f}ms'.format(min(val.success) if len(val.success) > 0 else 0),
                r'{:.3f}ms'.format(max(val.success) if len(val.success) > 0 else 0),
            )

        Console(width=800).print(table)


class TaskInterface(Utils, RunnableInterface):

    def __init__(self, publisher: PublishWithBuffer):

        self._publisher = publisher

    def success(self, name: str, resp_time: int):

        self._publisher.send(
            (name, r'success', resp_time,)
        )

    def failure(self, name: str, resp_time: int):

        self._publisher.send(
            (name, r'failure', resp_time,)
        )

    async def run(self):
        raise NotImplementedError()


class Runner(Utils, FunctorInterface):

    def __init__(self, task_cls: TaskInterface):

        global SIGNAL_PROTOCOL, SIGNAL_PORT

        self._task_cls = task_cls
        self._publisher = PublishWithBuffer(f'{SIGNAL_PROTOCOL}://localhost:{SIGNAL_PORT}', False)

    async def __call__(self, times, task_num):

        self._publisher.open()

        for _ in range(times):

            tasks = MultiTasks()

            for _ in range(task_num):
                tasks.append(self._task_cls(self._publisher).run())

            await tasks

        await self._publisher.safe_close()


class Launcher(command.Launcher):
    pass


class Daemon(command.Daemon):

    def __init__(self, child_num=2, report_cls=Reporter):

        super().__init__(child_num, False)

        self._report_cls = report_cls

    async def _run(self):

        with self._report_cls() as reporter:

            async for _ in AsyncCirculator():

                self._check_processes()

                if not self.is_active():
                    break

                await reporter.handle_message()

            reporter.print_report()

    def __call__(self):

        if self._fork_processes():
            Utils.run_until_complete(self._run())
            sys.exit(0)
