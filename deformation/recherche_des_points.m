
format long
in = fopen('Polytech_maillage/mesh/.mesh','r');

point = 'Vertices';

while ~strcmp(fgetl(in),point)
end

nb_point = str2num(fgetl(in));
disp(nb_point)
mat=zeros(nb_point,3);

for i=1:nb_point
    disp(i)
    mat(i,:) =str2num(fgetl(in));
end
