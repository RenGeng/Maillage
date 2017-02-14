
%DEFORMATION AFFINE

function [f] = affine(Pcontrole,v,NewP)
%Pi = points en entrée à déplacer, Ps= points deplacés, NewP nouveau point,
%v= points consiédé vecteur ligne

nbPtsControle=length(Pcontrole(:,1));
 
%initialisation du vecteur colonne contenant les poids
%Sur chaque colonne on a les wi correspond au v
%La 1ere ligne contient tous les v
wx=zeros(nbPtsControle,1);
wy=zeros(nbPtsControle,1);

alpha=1; %%ALPHA ??
 
%%On calcule les wi%%
%boucle pour chaque point de controle
    for i=1:nbPtsControle
        
        %vecteur avec coordonnees des points de controle
        Pi=Pcontrole(i,:);
        
        if Pi~=v
            %Calcul du poids en coordonnées x et y
            wx(i,1)=1/(abs(Pi(1,1))-v(1,1)).^(2*alpha);
            wy(i,1)=1/(abs(Pi(1,2))-v(1,2)).^(2*alpha);
        end
        
    end      
   
%W est le vecteur poids avec les coordonnées x et y
W=[wx wy];

%%On calcule les pî et les qî, pour cela on calcule d'abord les q étoile
%%(qx)  et p étoile (px)

%Somme des Wi
somWi=[sum(W(1,:));sum(W(2,:))];

%Somme des Wi*Pi
somwipi=zeros(1,2);

for i=1:nbPtsControle
    somwipi(1,1)=W(1,i)*Pcontrole(1,i)+somwipi(1,1);
    somwipi(1,2)=W(2,i)*Pcontrole(2,i)+somwipi(1,2);
end

%Somme des Wi*qi
somwiqi=zeros(1,2);

for i=1:nbPtsControle
    somwiqi(1,1)=W(1,i)*NewP(1,i)+somwiqi(1,1);
    somwiqi(1,2)=W(2,i)*NewP(2,i)+somwiqi(1,2);
end

%On peut donc calculer q étoile et p étoile
px=[somwipi(1,1) somwipi(1,2)];
qx=[somwiqi(1,1) somwiqi(1,2)];

%On peut maintenant calculer les pi chapeau (pich) et qi chapeau (qich)
pich(:,1)=Pcontrole(:,1)-px(1,1);
pich(:,2)=Pcontrole(:,2)-px(1,2);
qich(:,1)=NewP(:,1)-qx(1,1);
qich(:,2)=NewP(:,2)-qx(1,2);

%On calcule maintenant Aj et fa(v)
%f=((v-px)*inv(sum(pich(1:nbPtsControle)'*W(1:nbPtsControle)*pich(1:nbPtsControle)))*sum(W(1:nbPtsControle)*pich(1:nbPtsControle)'*qich(1:nbPtsControle)))+qx;
f=(v-px)*inv(pich'*W*pich)*W*pich'*qich+qx;

 
end

