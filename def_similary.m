function [f] = def_similary(P,v,Q)
%P=points controle(p1, p2, ...,pn) v=point (x,y) Q=nouveau points
%correspondant au pi (q1 q2 ... qn)

alpha=1;
n=length(P);
w=zeros(1,n);

for i=1:n
    if P(i,:)==v %pas sur
        w(i)=0;
    else
        w(i)=1/(norm(P(i,:)-v))^(2*alpha);
    end
end

%p et q étoile, px, qx 
px=zeros(1,2);
qx=zeros(1,2);
somwipi=[0 0];
somwiqi=[0 0];
somwi=0;

%On calcule les p et q étoile
for i=1:n
    somwipi=w(i)*P(i,:)+somwipi;
    somwiqi=w(i)*Q(i,:)+somwiqi;
    somwi=w(i)+somwi;
end

px=somwipi/somwi;
qx=somwiqi/somwi;

%calcule des pi et qi chapeau

pchap=zeros(n,2);
qchap=zeros(n,2);

for i=1:n
    pchap(i,:)=P(i,:)-px;
    qchap(i,:)=Q(i,:)-qx;
end

%Calcule de nu
nu=0;
for i=1:n
    nu=w(i)*pchap(i,:)*pchap(i,:)'+nu;
end

%Calcule de Ai
A2=zeros(2,2);
A2(1,:)=v-px;
A2(2,:)=-ortho(A2(1,:));
A2=A2';
f1=zeros(1,2);

for i=1:n
    A1=zeros(2,2);
    A1(1,:)=pchap(i,:);
    A1(2,:)=-ortho(pchap(i,:));
    f1=qchap(i,:)*(1/nu)*w(i)*A1*A2+f1;
end

f1=f1+qx;
f=f1-v;
end

function [vect] = ortho(u)
    vect=zeros(1,2);
    vect(1,1)=-u(1,2);
    vect(1,2)=u(1,1);
end

