format long
in = fopen('deformation/Polytech_maillage/mesh/man.mesh','r');

point = 'Vertices';

while ~strcmp(fgetl(in),point)
end

nb_point = str2num(fgetl(in));
disp(nb_point);
mat=zeros(nb_point,3);

for i=1:nb_point
    mat(i,:) =str2num(fgetl(in));
end

V = mat(:,1:2);
P=zeros(5,2);
P(1,:)=V(100,:);
P(2,:)=V(600,:);
P(3,:)=V(1100,:);
P(4,:)=V(1600,:);
P(5,:)=V(2100,:);
Q=zeros(5,2);
Q(1,:)=0.2*V(100,:);
Q(2,:)=0.2*V(600,:);
Q(3,:)=0.3*V(1100,:);
Q(4,:)=0.3*V(1600,:);
Q(5,:)=0.4*V(2100,:);
ptssol_affine=zeros(length(V),2);
ptssol_similary=zeros(length(V),2);
ptssol_rigid=zeros(length(V),2);
ind=0;

for i=1:length(V)
    cond=0;
    for j=1:length(P)
        if V(i,:)==P(j,:)
            ind=j;
            cond=1;
        end
    end
    if cond==0
        ptssol_affine(i,:)=affine2(P,V(i,:),Q);
        ptssol_similary(i,:)=def_similary(P,V(i,:),Q);
        ptssol_rigid(i,:)=rigid(P,V(i,:),Q);
    else
        ptssol_affine(i,:)=Q(ind,:)-P(ind,:);
        ptssol_similary(i,:)=Q(ind,:)-P(ind,:);
        ptssol_rigid(i,:)=Q(ind,:)-P(ind,:);
    end
        
end

figure(1)
plot(ptssol_affine(:,1),ptssol_affine(:,2),'.k');
title('Affine');

figure(2)
plot(ptssol_similary(:,1),ptssol_similary(:,2),'.k');
title('Similary');

figure(3)
plot(ptssol_rigid(:,1),ptssol_rigid(:,2),'.k');
title('Rigid');

figure(4)
plot(V(:,1),V(:,2),'.k');
title('Original');











