import qrenderdoc as qrd

# https://renderdoc.org/docs/python_api/ui_extensions.html
def register(version: str, ctx: qrd.CaptureContext):
    ctx.Extensions().RegisterContextMenu(qrd.ContextMenu.EventBrowser_Event, ["Debug Compute Shader"], debugComputeShader)

def unregister():
    print("Unregistering empty extension")

def debugComputeShader(ctx: qrd.CaptureContext, data):
  print("debugComputeShader")
