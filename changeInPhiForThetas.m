%changeInPhiForThetas
M = 3.85554;
R = .08;
L = .25;
beta = 120;
alpha = 40;
%I = .25*M*R^2 +(1/3)*M*L^2;
%J =  0.5*M*R^2;
J = 3;
I = 10;
thetas = [1:360];
dphi = 1;
for q = thetas
    i = (q*pi)/180;
    S = -(2^(-1/2))*sin(beta)*((cos(alpha)*sin(beta))+ sin(alpha)*cos(beta)*cos(i));
    T = cos(alpha)*cos(beta) - sin(alpha)*sin(beta)*cos(i);
    dphidtheta = ((J/I)*S)/((T-1)*(1- T +(J/I)*(1+T))*(1+T)^(1/2));
    dphi(q) = dphidtheta;
end
plot(thetas, dphi);
