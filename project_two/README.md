Monte Carlo simulation
Conceptual elements
    (1) Must include a monte carlo simulation of discrete elements (say particles, atoms, stars).
    (2) must include an evolution based on an 2nd order ODE (evolution of trajectory under a force, or state evolution) 
    (3) There must be opportunities for probabilistic interactions (say surface interaction which may have specular or diffuse reflection, or 
        interaction probability between particles, decay probability, etc)
    (4) Must identify a key result that summarizes the properties of the discrete elements. (e.g. spatial distribution and type of particle hitting a detector,
        mass distribution after evolution of gravitational n-body problem, etc). 
    (5) Must identify properties of the simulation and result that can be
        validated based on physical expectation (e.g. symmetries, conservations, etc). 

Plan: Simulate particles
Evolution of state?
Must be able to just install my package, and run a command, and then it'll make everything run

Neutrino collides with liquid argon atom (don't worry about cross section stuff)
Probability of it being electron neutrino or muon neutrino (only doing 2 flavors)
Depending on what type it is, there's some probability for what the final state is
Depending on what is produces, we have an electric field that will curve the products into the field cage
Solve the ODE to find the x, y, z value of the final products at each point in time and make a 3D event display plot!!!!