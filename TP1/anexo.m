clear all;
clc;

Padron=99999; % Padrón de un integrante del grupo

Thot=Padron/100+300; %°C
Tamb=20; % temperatura ambiente en °C

ni=90; %nodos coordenada angular
nj=20; %nodos coordenada radial
n=ni*nj; % nodos totales

rext=0.250; % radio externo del tubo en metros
wt=0.015; % espesor de la pared del tubo en metros
rint=rext-wt; % radio interno del tubo en metros
dr=wt/(nj-1); % delta r de la malla en metros

ncc=round(0.04*(ni-1)/(2*pi*rint)); %variable entera auxiliar

T=zeros(ni,nj);
b=zeros(n,1);
A=zeros(n,n);

for i=1:ni

	% Aplico condiciones de contorno
	% j=1 - nodos internos
	kx=1+nj*(i-1);
	A(kx,kx)=1;
	if(i<=ncc||i>ni-ncc+1)
		b(kx)=Thot*0.931;
	else
	
	b(kx)=Tamb;

	end
	
	for j=2:nj-1

	% Índices de los coeficientes de las ecuaciones
        kx=j+nj*(i-1);
        kn=j+1+nj*(i-1);
        ks=j-1+nj*(i-1);
        ke=j+nj*i;
        kw=j+nj*(i-2);
        if(ke>n)
            ke=ke-n;
        end
        if(kw<0)
            kw=kw+n;
        end

	% Coeficientes de las ecuaciones
        rj=rint+dr*(j-1);
        df=2*pi*rj/(ni-1);
        cn=1/dr^2+1/(2*dr*rj);
        ce=1/(rj^2*df^2); 
        cs=1/dr^2-1/(2*dr*rj);
        cw=1/(rj^2*df^2);
        cx=-2/dr^2-2/(rj^2*df^2);
        ci=0;

	%Matriz del sistema
        if(ke<kx)
            A(kx,ke)=ce;
        end
        if(kw<kx)
            A(kx,kw)=cw;
        end

        A(kx,ks)=cs;
        A(kx,kx)=cx;
        A(kx,kn)=cn;

        if(ke>kx)
            A(kx,ke)=ce;
        end
        if(kw>kx)
            A(kx,kw)=cw;
        end

        %Vector terminos independientes
        b(kx)=ci;

    end

    % Aplico condiciones de contorno
    % j=nj - nodos externos
    kx=nj+nj*(i-1);
    A(kx,kx)=1;
    if(i<=ncc||i>ni-ncc+1)
        b(kx)=Thot;
        else
        b(kx)=Tamb;
        end
    end
    
% Resuelvo el SEL A*x=b por el método SOR
x=solver_SOR(A,b);

% Resuelvo el SEL A*x=b por el método Gauss Seidel
x=solver_GS(A,b);

% Recupero la solución del sistema
for i=1:ni
	for j=1:nj
		kx=j+nj*(i-1); %fila-columna
		T(i,j)=x(kx);
	end
end
