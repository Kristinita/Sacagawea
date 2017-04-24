# -*- coding: utf-8 -*-
# @Author: Keith Hall
# @Date: 2017-04-24 06:43:14
# @Last Modified time: 2017-04-24 20:50:09
import subprocess

import sublime
import sublime_plugin


class SacagaweaStandardoCommand(sublime_plugin.TextCommand):

    def run(self, edit, seconds=10):
        self.print_seconds(sublime.active_window().new_file(), seconds)

    def print_seconds(self, view, seconds):
        mpg_command = ["mpg123", "-q", "beep-09.mp3"]
        text = ''
        if seconds >= 0:
            text = str(seconds)
            if seconds == 10:
                text += ''
            sublime.set_timeout_async(
                lambda: self.print_seconds(
                    view, seconds - 1), 1000)
            if seconds == 5:
                text += ' seconds'
                subprocess.Popen(mpg_command, shell=True)
            if seconds == 0:
                subprocess.Popen(mpg_command, shell=True)
                text = 'Time over!'
                sublime.set_timeout_async(
                    lambda: view.window().run_command('force_quit'), 5000)

        view.run_command(
            'append', {
                'characters': text + '\n', 'scroll_to_end': True})
