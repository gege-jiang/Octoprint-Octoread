import octoprint.plugin

class HelloWorldPlugin(octoprint.plugin.StartupPlugin,
                       octoprint.plugin.TemplatePlugin):
    def on_after_startup(self):
        self._logger.info("Hello World!")

__plugin_implementation__ = HelloWorldPlugin()
__plugin_name__ = "Octoread"
__plugin_pythoncompat__ = ">=3.7,<4"