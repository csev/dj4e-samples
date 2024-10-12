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
        zf = request.FILES['zip']
        zfile = zipfile.ZipFile(zf)
        idvalue = 0
        pieces = list()
        for fname in zfile.namelist():
            print(fname)
            idvalue = idvalue + 1
            piece = dict()
            piece['idvalue'] = idvalue
            piece['fname'] = fname

            isdir = zipfile.Path(root=zfile, at=fname).is_dir()
            if isdir : 
                piece['folder'] = isdir
                pieces.append(piece)
                continue
            with zfile.open(fname) as hand:
                data = hand.read()
                piece['size'] = len(data)
                print(data[:100])
                if fname.endswith('.jpg') : 
                    piece['type'] = 'jpg'
                    data_base64 = base64.b64encode(data)  # encode to base64 (bytes)
                    data_base64 = data_base64.decode()
                    htm = '<img src="data:image/jpeg;base64,' + data_base64 + '"><br/>'
                    piece['html'] = htm
                elif fname.endswith('.xml') :
                    piece['type'] = 'xml'
                    htm = "<pre>\n" + html.escape(data.decode()) + "\n</pre>\n"
                    piece['html'] = htm
                elif fname.endswith('.html') :
                    piece['type'] = 'html'
                    piece['html'] = data.decode()

            pieces.append(piece)

        context = { 'title': zf, 'pieces': pieces }
        return render(request, 'zip/zipdump.html', context)

