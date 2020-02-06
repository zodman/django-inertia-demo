
def share(request, key, value):
    request.session.setdefault("share",{})
    request.session["share"][key]=value