import gprMax

n_runs = 10
scenes = []

for n in range(0, n_runs):

    scene = gprMax.Scene()
    dxdydz = gprMax.Discretisation(p1=(1, 1, 1))
    domain = gprMax.Domain(p1=(5e-2, 5e-2, 50e-2))
    tw = gprMax.TimeWindow(time=60e-9)

    title = gprMax.Title('Wire antenna - half-wavelength dipole in free-space')

    # adjust centre frequency for each simulation
    freq = 1e9 + 1e6 * n
    waveform = gprMax.Waveform(type='gaussian', amp='1', freq=freq, id='mypulse')
    tl = gprMax.TransmissionLine(polarisation='z', p1=(0.025, 0.025, 0.100), resistance=73, waveform_id='mypulse')

    ## 150mm length
    e1 = gprMax.Edge(p1=(0.025, 0.025, 0.025), p2=(0.025, 0.025, 0.175), material_id='pec')

    ## 1mm gap at centre of dipole
    e2 = gprMax.Edge(p1=(0.025, 0.025, 0.100), p2=(0.025, 0.025, 0.101), material_id='free_space')

    scene.add(dxdydz)
    scene.add(domain)
    scene.add(timewindow)
    scene.add(title)
    scene.add(waveform)
    scene.add(tl)
    scene.add(e1)
    scene.add(e2)

    scenes.append(scene)

gprMax.run(scenes=scenes, preserve_geometry=True)
