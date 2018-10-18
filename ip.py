import sublime, sublime_plugin


class AddHostname(sublime_plugin.TextCommand):
    def run(self, edit):
        from socket import gethostbyaddr
        sublime.status_message('Getting hostname....')
        for region in self.view.sel():
            if not region.empty():
                text = self.view.substr(region).strip()
                result = '{0} -> {1}'.format(text, gethostbyaddr(text)[0])
                self.view.replace(edit, region, result)
                sublime.status_message('Complete!')


class AddIp(sublime_plugin.TextCommand):
    def run(self, edit):
        from socket import gethostbyname
        sublime.status_message('Getting IP.....')
        for region in self.view.sel():
            if not region.empty():
                text = self.view.substr(region).strip()
                result = '{0} -> {1}'.format(text, gethostbyname(text))
                self.view.replace(edit, region, result)
                sublime.status_message('Complete!')


class AddIps(sublime_plugin.TextCommand):
    def run(self, edit):
        from socket import gethostbyname_ex
        sublime.status_message('Getting IPs.....')
        for region in self.view.sel():
            if not region.empty():
                text = self.view.substr(region).strip()
                result = '{0} -> {1}'.format(text, ', '.join(str(ip) for ip in gethostbyname_ex(text)[2]))
                self.view.replace(edit, region, result)
                sublime.status_message('Complete!')