import pandas as pd
x={
    'B (T)': [0.02, 0.20],
    'H (Av/m)': [20, 40]
}
y={
    'B (T)': [2, 4],
    'H (Av/m)': [20, 40]
}
x=pd.DataFrame(x)
y=pd.DataFrame(y)


datosprueba1=[x,'']
datosprueba2=[y,'']




def sacarH(datosMu,flujoE=1,SC=1, factorApilado=1):
    #Saco B3 realmente
    datos=datosMu[0]
    B=flujoE/(factorApilado*SC)
    
    if datosMu[1]=='ecuacion':
        a=datosMu[0]['a']
        b=datosMu[0]['b']
        if (a-b*B)==0:
            H=1
            st.write('Hay un problema con la fórmula')
        else:
            H= abs(B)/(a-b*abs(B))
    elif B==0:
        H=0
    else:
        menorB=0
        mayorB=0
        menorH=0
        mayorH=0
        b_array = datos['B (T)'].to_numpy()
        h_array = datos['H (Av/m)'].to_numpy()
        b_array,h_array= bubble_sort(b_array,h_array)
        print(h_array)
        print(b_array)
        if B<b_array[0]:
            menorB=b_array[0]
            menorH=h_array[0]
            mayorB=b_array[1]
            mayorH=h_array[1]
        elif B>b_array[len(b_array)-1]:
            menorB=b_array[len(b_array)-2]
            menorH=h_array[len(b_array)-2]
            mayorB=b_array[len(b_array)-1]
            mayorH=h_array[len(b_array)-1]
        else:
            for i in range(len(b_array)):
                if b_array[i]<abs(B):
                    menorB=b_array[i]
                    menorH=h_array[i]

                if b_array[i]>abs(B):
                    mayorB=b_array[i]
                    mayorH=h_array[i]
                    break
        H = menorH + (B - menorB) * (mayorH - menorH) / (mayorB - menorB)
        #print(menorB)
        #print(mayorB)

    #print(B)
    #print(H)
    return H

def bubble_sort(arr, otro):

    # Outer loop to iterate through the list n times
    for n in range(len(arr) - 1, 0, -1):

        # Inner loop to compare adjacent elements
        for i in range(n):
            if arr[i] > arr[i + 1]:

                # Swap elements if they are in the wrong order
                swapped = True
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                otro[i], otro[i + 1] = otro[i + 1], otro[i]
    return arr, otro


sacarH(datosprueba1)
sacarH(datosprueba2)
sacarH(datosprueba1,0)