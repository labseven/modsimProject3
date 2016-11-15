function [theta, deltaPhi] = kaneScherModel (theta, phi)
M = 3.85554;
R = .08;
L = .25;
beta = 120;
alpha = 40;
%I = .25*M*R^2 +(1/3)*M*L^2;
%J =  0.5*M*R^2;
J = 3;
I = 10;
S = -(2^(-1/2))*sin(beta)*((cos(alpha)*sin(beta))+ sin(alpha)*cos(beta)*cos(theta));
T = cos(alpha)*cos(beta) - sin(alpha)*sin(beta)*cos(theta);
dphidtheta = ((J/I)*S)/((T-1)*(1- T +(J/I)*(1+T))*(1+T)^(1/2));
end