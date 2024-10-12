from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
import zipfile
import base64
import html

# Create your views here.

class UploadView(View) :
    def get(self, request):
        return render(request, 'zip/upload.html')

    def post(self, request):
        retval = """<h1>Yada</h1>
<script>
function toggle(elem) {
  var x = document.getElementById(elem);
  if (x.style.display === "none") {
    x.style.display = "block";
  } else {
    x.style.display = "none";
  }
}
</script>
"""
        print(request.FILES)
        zf = request.FILES['zip']
        print(zf)
        zfile = zipfile.ZipFile(zf)
        idvalue = 0
        for fname in zfile.namelist():
            print(fname)
            idvalue = idvalue + 1
            retval += "<li>" + fname

            isdir = zipfile.Path(root=zfile, at=fname).is_dir()
            print(isdir)
            if isdir : 
                retval += " (folder) </li>\n"
                continue
            with zfile.open(fname) as hand:
                data = hand.read()
                print(data[:100])
                if fname.endswith('.jpg') : 
                    retval += "<br>"
                    data_base64 = base64.b64encode(data)  # encode to base64 (bytes)
                    data_base64 = data_base64.decode()
                    htm = '<img src="data:image/jpeg;base64,' + data_base64 + '"><br/>'
                    retval += htm
                elif fname.endswith('.xml') :
                    retval += "<button onclick=\"toggle('" + str(idvalue) + "');\">Toggle</button>"
                    retval += "<br><div id=\"" + str(idvalue) + "\" style=\"display: none;\">"
                    htm = "<pre>\n" + html.escape(data.decode()) + "\n</pre>\n"
                    retval += htm
                    retval += "</div>\n"
                elif fname.endswith('.html') :
                    retval += "<button onclick=\"toggle('" + str(idvalue) + "');\">Toggle</button>"
                    retval += "<br><div id=\"" + str(idvalue) + "\" style=\"display: none;\">"
                    retval += data.decode()
                    retval += "</div>\n"

            retval += "</div></li>\n"


        return HttpResponse(retval);

