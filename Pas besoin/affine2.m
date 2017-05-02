function [f] = affine2(P,v,Q)
%P=points controle(p1, p2, ...,pn) v=point (x,y) Q=nouveau points
%correspondant au pi (q1 q2 ... qn)

alpha=1;
n=length(P);
w=zeros(1,n);

for i=1:n
    w(i)=1/(norm(P(i,:)-v))^(2*alpha);
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

%Calcule de fa(v)
M1=zeros(2,2);
M2=zeros(2,2);

for i=1:n
    M1=pchap(i,:)'*w(i)*pchap(i,:)+M1;
    M2=w(i)*pchap(i,:)'*qchap(i,:)+M2;
end

M1=inv(M1);

%On calcule fa(v)

f1=(v-px)*M1*M2+qx;
f=f1-v;

end
