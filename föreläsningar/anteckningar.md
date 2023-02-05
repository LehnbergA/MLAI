


# Anteckningar från föreläsningar



## Vecka 5 torsdag 2/2

1. Data preparation
2. Wavelets

### Data preparation:
Basic shit...
Wavelet transform kan användas för att göra data mindre noisy
Samt dimensionsreducering

-- Borde kolla på outliers... T.ex. k-means, PCA, cock length

### Wavelet
Ofta osäkerhet i data.
Vi vill kunna filtrera och komprimera data.
Generell ide är att ta bort små skillnader (vi antar att små koefficienter hör till noise)

FFT = bra för frekensupplösning, dålig för positionsbestämning
 = bra information dålig på tid

STFT = ok info ok tid

HAARWavelet är beroende på frekvens. Först bestäms position/tid (liten info om frekvensen)
Sedan får vi successivt mer info om frekvensen.

Heisenbergs osäkerhetsprincip (tradeoff)

I machine learning finns ett räkneexempel som är lämpligt att börja med under discrete wavelet transform.
(finns beskrivet iaf, exempel kanske någon annanstans). Kommer def behöva läsa wavelets.pdf...

Gör två "svep"
Finns ett script att utgå från

Vi kommer ha uppgt 1 och 2 att jobba med fram till sommaren lol

Glöm inte kolla GPU. Använd "Cuda"


----------------- Från Wavelets: \
Ex 1.4: Om vi hjar en stegfunktion motsvarar sj värdet s vid steg j. rj motsvarar tiden/steget/x-axelns värden för steg j. \
Ex 1.12: \
Utgå från 1.4 s = (3,  1, 0, 4,  8, 6, 9, 9). Initiering a3 = s.\
Svep 1: a(3-1) = 3+1/2, 0+4/2, 8+6/2, 9+9/2 = (2, 2, 7, 9) \
c(3-1) = 3-1/1, 0-4/2, 8-6/2, 9-9/2 = (1, -2, 1, 0) \
Detta ger s(3-1) = (a(3-1); s(3-1)) = (2, 2, 7, 9; 1, -2, 1, 0). Detta är ett Svep.\
\
Svep 2: a(3-2) = (2+2/2, 7+9/2) = (2, 8)\
c(3-2) = (2-2/2, 7-9/2) = (0, -1)\
s(3-2) = (a(3-2); c(3-2); c(3-1)) =(2, 8; 0, -1; 1, -2, 1, 0) \
\
Svep 3: s(3-3) = (a(3-3); c(3-3); c(3-2); c(3-1)) = (5; -3; 0; -1; 1; -2; 1 ;0) \
\
Tolkning: a är approximering av f genom de observerade värdena. c är wavelet coefficienterna som är ytterligare en approximation av f men uttryckt i monotont minskande frekvenser. \
\
f = svep1 + svep2 + svep3. Se hur f representeras mha s(3-3) under 1.3.2.9 s.20. Psi[0,1[ = Haars wavelet funktion = phi[0,1/2[ - phi[1/2, 1[   (där phi är någon stegfunktion) 





