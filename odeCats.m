%odeCats
phiI = 0;
thetas = [0:0.2:(2*pi)];
[theta, phi] = ode45(@kaneScherModel, thetas, phiI);
plot (theta, phi)