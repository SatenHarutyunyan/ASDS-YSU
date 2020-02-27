from automl import profile, system

profile = profile.Profile()
profile.data = "...."
profile.model = "classification"

system = system.System(profile)

# system.run()
