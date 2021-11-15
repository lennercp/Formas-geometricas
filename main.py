from plana import *
from tridimensional import *
from tkinter import *
from PIL import Image, ImageTk

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
    if formas.get() == 1:
        widgetsList = atributosFormas['quadrado']
        forma = 'quadrado'
    elif formas.get() == 2:
        widgetsList = atributosFormas['retangulo']
        forma = 'retangulo'
    elif formas.get() == 3:
        widgetsList = atributosFormas['circulo']
        forma = 'circulo'
    elif formas.get() == 4:
        widgetsList = atributosFormas['cubo']
        forma = 'cubo'
    elif formas.get() == 5:
        widgetsList = atributosFormas['esfera']
        forma = 'esfera'
    else:
        widgetsList = atributosFormas['paralelepipedo']
        forma = 'paralelepipedo'
        
    MostrarWidgets(widgetsList, frameAtributos)

def ApagarFrames(frame):
    frames = tela.pack_slaves()

    if frame in frames:
        for f in range(frames.index(frame), len(frames)):
            for widget in frames[f].pack_slaves():
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

    if atributos.get() == 1:
        numeroEntry = numerosEntry[forma]['perimetro']
        atributo = 'perimetro'
    elif atributos.get() == 2:
        numeroEntry = numerosEntry[forma]['area']
        atributo = 'area'
    elif atributos.get() == 3:
        numeroEntry = numerosEntry[forma]['diagonal']
        atributo = 'diagonal'
    else:
        numeroEntry = numerosEntry[forma]['volume']
        atributo = 'volume'
    
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
quadradoFoto = ImageTk.PhotoImage(Image.open("img/quadrado.png").resize((100,100)))
quadrado = Radiobutton(frameFormas, text='quadrado', image=quadradoFoto, variable=formas, value=1, command=Formas) 

retanguloFoto = ImageTk.PhotoImage(Image.open("img/retangulo.png").resize((100,70)))
retangulo = Radiobutton(frameFormas, text='retangulo', image=retanguloFoto, variable= formas, value=2, command=Formas) 

circuloFoto = ImageTk.PhotoImage(Image.open("img/circulo.png").resize((70,70)))
circulo = Radiobutton(frameFormas, image=circuloFoto, variable=formas, value=3, command=Formas) 

#formas 3D
cuboFoto = ImageTk.PhotoImage(Image.open("img/cubo.png").resize((70,70)))
cubo = Radiobutton(frameFormas, image=cuboFoto, variable=formas, value=4, command=Formas) 

esferaFoto = ImageTk.PhotoImage(Image.open("img/esfera.png").resize((70,70)))
esfera = Radiobutton(frameFormas, image=esferaFoto, variable=formas, value=5, command=Formas) 

paralelepipedoFoto = ImageTk.PhotoImage(Image.open("img/paralelepipedo.png").resize((100,70)))
paralelepipedo = Radiobutton(frameFormas, image=paralelepipedoFoto, variable=formas, value=6, command=Formas) 

#atributos planos
perimetroButton = Radiobutton(frameAtributos, text="Perimetro", variable=atributos, value=1, command= createEntry)
areaButton = Radiobutton(frameAtributos, text="Área", variable=atributos, value=2, command= createEntry)
diagonalButton = Radiobutton(frameAtributos, text="Diagonal", variable=atributos, value=3, command= createEntry)

#atributos 3D
volumeButton = Radiobutton(frameAtributos, text="Volume", variable=atributos, value=4, command= createEntry)
diagonalButton = Radiobutton(frameAtributos, text="Diagonal", variable=atributos, value=3, command= createEntry)

#dicionarios
formasGeometricas = {
    'plano': [quadrado, retangulo, circulo],
    'tresD': [cubo, paralelepipedo, esfera]
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
        'diagonal': ['area']
    }, 
    'paralelepipedo':{
        'volume': ['lado1', 'lado2', 'lado3'], 
        'diagonal': ['lado1','lado2','lado3']
    }
}

tela.mainloop()