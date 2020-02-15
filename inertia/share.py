

def share(request, key, value):
    request.session.setdefault("share",{})
    request.session["share"][key]=value

# used in pingcrm ... 
def share_flash(request, success=False, error=False, errors = []):
    share(request, "flash",{'success':success,'error':error})
    if errors:
        share(request, "errors",errors)