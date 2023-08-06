import tempfile
import webbrowser
from urllib.parse import urljoin

from classiq.interface.generator.result import GeneratedCircuit
from classiq.interface.server import routes

from classiq._internals.api_wrapper import ApiWrapper
from classiq._internals.async_utils import syncify_function

_LOGO_HTML = '<p>\n    <img src="https://classiq-public.s3.amazonaws.com/logo/Green/classiq_RGB_Green.png" alt="Classiq logo" height="40">\n    <br>\n  </p>\n'


async def _show_interactive(
    self: GeneratedCircuit, jupyter=False, web_app: bool = False
) -> None:
    if self.interactive_html is None:
        raise ValueError("Missing interactive html")

    if jupyter:  # show inline in jupyter
        # We assume that we're inside a jupyter-notebook
        # We cannot test it, since this is a part of the interface, while the jupyter-related code is in the SDK
        from IPython.core.display import HTML, display  # type: ignore

        h = HTML(self.interactive_html.replace(_LOGO_HTML, ""))
        display(h)

    if web_app:
        circuit_id = await ApiWrapper.call_analyzer_app(self)
        app_url = urljoin(routes.ANALYZER_FULL_FE_APP, str(circuit_id.id))
        print(
            f"If a browser doesn't automatically open, please visit the url: {app_url}"
        )
        webbrowser.open_new_tab(app_url)

    else:  # open web browser
        with tempfile.NamedTemporaryFile(
            "w", delete=False, suffix="_interactive_circuit.html"
        ) as f:
            url = f"file://{f.name}"
            f.write(self.interactive_html)
        webbrowser.open(url)


GeneratedCircuit.show_interactive = syncify_function(_show_interactive)  # type: ignore[attr-defined]
GeneratedCircuit.show_interactive_async = _show_interactive  # type: ignore[attr-defined]
