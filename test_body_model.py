import pyvista as pv

mesh = pv.read('male.glb')
plotter = pv.Plotter()
plotter.set_background('white')
plotter.add_mesh(mesh, color='lightblue', show_edges=False)
plotter.show()
