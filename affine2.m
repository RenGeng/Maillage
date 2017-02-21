function [f] = affine2(P,v,Q)
%P=points controle(p1, p2, ...,pn) v=point (x,y) Q=nouveau points
%correspondant au pi (q1 q2 ... qn)

n=length(P(1,:));
W=zeros(1,n);

for i=1:n
    if P(:,i)==v %pas sur
        w(i)=1/(norm(Q(:,i)-v))^2;
    else
        w(i)=1/(norm(P(:,i)-v))^2;
    end
end

%p et q étoile, px, qx 
px=zeros(2,1);
qx=zeros(2,1);
somwipi=[0;0];
somwiqi=[0;0];
somwi=0;

%On calcule les p et q étoile
for i=1:n
    somwipi=w(i)*P(:,i)+somwipi;
    somwiqi=w(i)*Q(:,i)+somwiqi;
    somwi=w(i)+somwi
end


px=somwipi/somwi;
qx=somwiqi/somwi;


%calcule des pi et qi chapeau

pchap=zeros(2,n);
qchap=zeros(2,n);

for i=1:n
    pchap(:,i)=P(:,i)-px
    qchap(:,i)=Q(:,i)-qx;
end

%Calcule de fa(v)
M1=zeros(2,2);
M2=zeros(2,2);

for i=1:n
    M1=pchap(:,i)'*w(i)*qchap(:,i)+M1;
    M2=w(i)*pchap(:,i)'*qchap(:,i)+M2;
end
M1
det(M1)
M1=inv(M1);
M=M1*M2;

%On calcule fa(v)

f=(v-px)'*M+qx';
   

end

