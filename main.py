from plana import *
from tridimensional import *
from tkinter import *
from PIL import Image, ImageTk, ImageOps

tela = Tk()
tela.geometry('500x300+500+200')
tela.title('Tipos de formas')

frameTipoFormas = Frame(tela)
frameTipoFormas.pack(pady=7)

frameFormas = Frame(tela)

frameAtributos = Frame(tela)

frameEntrys = Frame(tela)

frameResultado = Frame(tela)

frameAlerta = Frame(tela)

tipoForma = IntVar()
formas = IntVar()
atributos = IntVar()

forma = ''
atributo = ''

def TipoFormas():
    if tipoForma.get() == 1:
        widgetsList = formasGeometricas['plano']
    else:
        widgetsList = formasGeometricas['tresD']
    
    MostrarWidgets(widgetsList, frameFormas)

def Formas():
    global forma
    widgestsdict = {1: 'quadrado',
                    2: 'retangulo',
                    3: 'circulo',
                    4: 'cubo',
                    5: 'esfera',
                    6: 'paralelepipedo'
                   }
    
    forma = widgestsdict[formas.get()]
    
    widgetsList = atributosFormas[forma]
        
    MostrarWidgets(widgetsList, frameAtributos)

def ApagarFrames(frame):
    frames = tela.pack_slaves()

    if frame in frames:
        for f in range(frames.index(frame), len(frames)):
            for widget in frames[f].pack_slaves():
                if len(widget.pack_slaves()) > 0:
                    if str(type(widget.pack_slaves()[1])) == "<class 'tkinter.Radiobutton'>":
                        widget.pack_forget()
                        continue

                if "<class 'tkinter.Frame'>" == str(type(widget)):
                    for widgetEntry in widget.pack_slaves():
                        widgetEntry.destroy()
                
                widget.pack_forget()
            frames[f].pack_forget()
    
    frame.pack()

def MostrarWidgets(widgetsList, frame):
    ApagarFrames(frame)

    frame.pack()

    for widget in widgetsList:
        widget.pack(side = LEFT)
    atributos.set(None)

def createEntry():
    global forma
    global frameEntrys
    global atributo

    ApagarFrames(frameEntrys)

    atributosdict = {1: 'perimetro',
                     2: 'area',
                     3: 'diagonal',
                     4: 'volume',}
    
    atributo = atributosdict[atributos.get()]
    
    numeroEntry = numerosEntry[forma][atributo]
    
    for textLabel in numeroEntry:
        frameEntry = Frame(frameEntrys)
        frameEntry.pack()

        Label(frameEntry, text=textLabel).pack(side= LEFT)
        e = Entry(frameEntry)
        e.bind('<Return>', lambda e: Calcular())
        e.pack(side=RIGHT)

    btnCalcular = Button(tela, text='Calcular', fg='red', command=Calcular).pack()

def ValoresEntry():
    frames = frameEntrys.pack_slaves()

    valores = []
    for frame in frames:
        for widget in frameResultado.pack_slaves():
            widget.destroy()
        frameResultado.pack_forget()

        try:
            valores.append(int(frame.children['!entry'].get()))
            
        except ValueError:
            if not frame.children['!entry'].get():
                mostrarAlerta('Preencha todos os campos!!')
            else:
                mostrarAlerta('Apenas números!!')
            break
    else:
        return valores
        
def Calcular():
    global forma
    global atributo
    
    valores = ValoresEntry()
    if valores is not None:
        resultado = eval(f'{forma.title()}().{atributo}(*valores)')
        MostrarResultado(atributo, resultado)


def MostrarResultado(atributo, resultado):
    frameResultado.pack()
    Label(frameResultado, text=f'{atributo}: {resultado:.2f}').pack()

def mostrarAlerta(mensagem):
    frameResultado.pack()
    Label(frameResultado, text=mensagem, fg='red').pack()


planaButton = Radiobutton(frameTipoFormas, text='Formas planas', variable=tipoForma, value=1, command=TipoFormas).pack(side=LEFT)

tresDButton = Radiobutton(frameTipoFormas, text='Formas 3D', variable=tipoForma, value=2, command=TipoFormas).pack(side=RIGHT)

#formas planas
frameQuadrado = Frame(frameFormas)
quadradoLabel = Label(frameQuadrado, text="     Quadrado").pack()
quadradoimage = Image.open("img/quadrado.png").resize((80,75))
quadradocut = ImageOps.crop(quadradoimage, (0,2,0,0))
quadradoFoto = ImageTk.PhotoImage(quadradocut)
quadrado = Radiobutton(frameQuadrado, text='quadrado', image=quadradoFoto, variable=formas, value=1, command=Formas).pack()

frameRetangulo = Frame(frameFormas)
retanguloLabel = Label(frameRetangulo, text="      Retangulo").pack(pady=(0,5))
retanguloimage = Image.open("img/retangulo.png").resize((100,70))
retangulocut = ImageOps.crop(retanguloimage, (0,3,0,0))
retanguloFoto = ImageTk.PhotoImage(retangulocut)
retangulo = Radiobutton(frameRetangulo, text='retangulo', image=retanguloFoto, variable= formas, value=2, command=Formas).pack()

frameCirculo = Frame(frameFormas)
circuloLabel = Label(frameCirculo, text="     Circulo").pack()
circuloimage = Image.open("img/circulo.png").resize((70,70))
circuloFoto = ImageTk.PhotoImage(circuloimage)
circulo = Radiobutton(frameCirculo, image=circuloFoto, variable=formas, value=3, command=Formas).pack() 

#formas 3D
frameCubo = Frame(frameFormas)
cuboLabel = Label(frameCubo, text="     Cubo").pack()
cuboimage = Image.open("img/cubo.png").resize((70,70))
cuboFoto = ImageTk.PhotoImage(cuboimage)
cuboFoto = ImageTk.PhotoImage(Image.open("img/cubo.png").resize((70,70)))
cubo = Radiobutton(frameCubo, image=cuboFoto, variable=formas, value=4, command=Formas).pack()

frameParalelepipedo = Frame(frameFormas)
paralelepipedoLabel = Label(frameParalelepipedo, text="      Paralelepipedo").pack()
paralelepipedoimage = Image.open("img/paralelepipedo.png").resize((70,70))
paralelepipedoFoto = ImageTk.PhotoImage(paralelepipedoimage)
paralelepipedoFoto = ImageTk.PhotoImage(Image.open("img/paralelepipedo.png").resize((100,70)))
paralelepipedo = Radiobutton(frameParalelepipedo, image=paralelepipedoFoto, variable=formas, value=6, command=Formas).pack() 

frameEsfera = Frame(frameFormas)
esferaLabel = Label(frameEsfera, text="      Esfera").pack()
esferaimage = Image.open("img/esfera.png").resize((70,70))
esferaFoto = ImageTk.PhotoImage(esferaimage)
esferaFoto = ImageTk.PhotoImage(Image.open("img/esfera.png").resize((70,70)))
esfera = Radiobutton(frameEsfera, image=esferaFoto, variable=formas, value=5, command=Formas).pack() 

#atributos planos
perimetroButton = Radiobutton(frameAtributos, text="Perimetro", variable=atributos, value=1, command= createEntry)
areaButton = Radiobutton(frameAtributos, text="Área", variable=atributos, value=2, command= createEntry)
diagonalButton = Radiobutton(frameAtributos, text="Diagonal", variable=atributos, value=3, command= createEntry)

#atributos 3D
volumeButton = Radiobutton(frameAtributos, text="Volume", variable=atributos, value=4, command= createEntry)
diagonalButton = Radiobutton(frameAtributos, text="Diagonal", variable=atributos, value=3, command= createEntry)

#dicionarios
formasGeometricas = {
    'plano': [frameQuadrado, frameRetangulo, frameCirculo],
    'tresD': [frameCubo, frameParalelepipedo, frameEsfera]
}

atributosFormas = {
    'quadrado': [perimetroButton, areaButton, diagonalButton],
    'retangulo': [perimetroButton, areaButton, diagonalButton],
    'circulo' : [perimetroButton, areaButton],
    'cubo':[volumeButton, diagonalButton], 
    'paralelepipedo':[volumeButton, diagonalButton], 
    'esfera':[volumeButton]
}

numerosEntry = {
    'quadrado': {
        'perimetro': ['lado'],
        'diagonal': ['area'],
        'area': ['lado']
    },
    'retangulo': {
        'area': ['lado1','lado2'],
        'diagonal' : ['area','lado1','lado2'],
        'perimetro' : ['lado1','lado2']

    },
    'circulo':{
        'area': ['raio'],
        'perimetro': ['raio']
    },
    'esfera':{ 
        'volume': ['raio']
    },
    'cubo':{
        'volume': ['lado'], 
        'diagonal': ['lado']
    }, 
    'paralelepipedo':{
        'volume': ['lado1', 'lado2', 'lado3'], 
        'diagonal': ['lado1','lado2','lado3']
    }
}

tela.mainloop()
