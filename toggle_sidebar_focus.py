import sublime
import sublime_plugin

class ToggleSidebarAndFocusCommand(sublime_plugin.WindowCommand):
    def run(self):
        if self.window.is_sidebar_visible():
            self.window.run_command("toggle_side_bar")
        else:
            self.window.run_command("toggle_side_bar")
            self.window.run_command("focus_side_bar")