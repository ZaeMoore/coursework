Welcome to the interactive neutrino simulation experience!
~A neutrino's best quality is its wiggles~

Simply download this package and install it to begin!

Plan: Simulate particles
Evolution of state?
Must be able to just install my package, and run a command, and then it'll make everything run

Neutrino collides with liquid argon atom (don't worry about cross section stuff)
Probability of it being electron neutrino or muon neutrino (only doing 2 flavors)
Depending on what type it is, there's some probability for what the final state is
Depending on what is produces, we have an electric field that will curve the products into the field cage
Solve the ODE to find the x, y, z value of the final products at each point in time and make a 3D event display plot!!!!

Pseudocode:

Main script, takes user input and passes parameters and accepted results from other scripts
final_state script does the monte carlo simulation to determine the flavor of the neutrino and the final state particles
after the interaction. Returns this data and the momentum of the final state particles to the main script
Main script passes this to another script that determines the trajectory of the final state particles in a detector with an electric field 
that directs these particles towards a pixel detector
Results: Location of hits on the pixel detector, histogram of flavor of neutrinos