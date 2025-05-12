import pyvista as pv 

filename = 'MALE.obj'

mesh = pv.read(filename)
plotter = pv.Plotter()
plotter.add_mesh(mesh, color='white', show_edges=True)
plotter.show()
