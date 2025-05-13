import pyvista as pv

filename = 'MALE.obj'

mesh = pv.read(filename)
plotter = pv.Plotter()
plotter.set_background('white')
plotter.add_mesh(mesh, color='lightblue', show_edges=False)
plotter.show()
