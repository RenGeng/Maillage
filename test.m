format long
in = fopen('deformation/Polytech_maillage/mesh/man.mesh','r');

point = 'Vertices';

while ~strcmp(fgetl(in),point)
end

nb_point = str2num(fgetl(in));
disp(nb_point)
mat=zeros(nb_point,3);

for i=1:nb_point
    mat(i,:) =str2num(fgetl(in));
end

V = mat(:,1:2);
P=V(1:3,:)';
Q=zeros(2,3);
Q(1,:)=0.99;
Q(2,:)=0.99;
newmesh=zeros(2,length(V));

for i=4:length(V)
    newmesh(:,i)=affine2(P,V(i,:)',Q);
end

%pichap'*wi*pichap impossible de l'inverser !