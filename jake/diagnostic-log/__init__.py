import qrenderdoc as qrd

# https://renderdoc.org/docs/python_api/ui_extensions.html
def register(version: str, ctx: qrd.CaptureContext):
    ctx.Extensions().RegisterWindowMenu(qrd.WindowMenu.Window, ["Diagnostic Log"], showDiagnosticLogWindow)

def unregister():
    print("Unregistering empty extension")

def showDiagnosticLogWindow(ctx: qrd.CaptureContext, data):
    ctx.ShowDiagnosticLogView()
