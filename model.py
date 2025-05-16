import pyvista as pv

class BodyModel:
    def __init__(self, model_path):
        self.model = pv.read(model_path)
        self.plotter = pv.Plotter()
        self.part_data = self.load_model()

    def load_model(self):
        return {
            "Node_0": "ankle : allows for movement and stability", 
            "Node_1": "elbow : allows for movement of the arm",
            "Node_2" : "foot : support body weight and facilitate movement", 
            "Node_3": "hand : malipulates objects",
            "Node_4" : "hand.001 : manipulates objects",
            "Node_5" : "head : protects the brain",
            "Node_6" : "knee : allows for movement and stability",
            "Node_7" : "knee :allows for movement and stability",
            "Node_8" : "left arm : allows for movement and manipulation",
            "Node_9" :"Male : the entire body",
            "Node_10" : "quad : allows for movement and stability",
            "Node_11" : "quad.001 allows for movement and stability",
            "Node_12" : "reproductive system to enable human reproduction",
            "Node_13": "right arm allows for movement and manipulation",
            "Node_14" : "shin :support weight bearing activities and facilitate movement",
            "Node_15" : "shin.001 : support weight bearing activities and facilitate movement",
            "Node_16" : "spine : protects the spinal cord",
            "Node_17" : "torso : protects the heart and lungs"
        }
    def _on_pick(self, *args):
        print("Picking callback triggered.")
        picked_mesh = args[0]
        
        if picked_mesh is None:
            print("No mesh picked.")
            return 
        
        picked_point = picked_mesh
        print(f"Picked point: {picked_point}")
        
        if isinstance(self.model, pv.MultiBlock):
            for i in range(self.model.n_blocks):
                part = self.model[i]
                if isinstance(part, pv.DataSet):
                    if part.equals(picked_mesh):
                        print("Match found Node_{i}.")
                                    
                        part_name = f"Node_{i}"
                        description = self.part_data.get(part_name, "No description available")
                        print(f"\nPicked part: {part_name}")
                        print(f"Function: {description}")
                        self.plotter.add_text(f"Picked part: {part_name}", position='upper_left', font_size=12, color='black')
                        return
            print("No matching part found.")
        else:
            print("You clicked the body model, but it is not a MultiBlock object.")
            description = self.part_data.get("Unknown part", "No description available")
            self.plotter.add_text(f"Picked part: Unknown part", position='upper_left', font_size=12, color='black')
        

    def plot_model(self):
        mesh = pv.read('male.glb')
        plotter = pv.Plotter()
        plotter.set_background('white')
        plotter.add_mesh(self.mesh, color='lightblue', show_edges=False)
    

    def run(self):
        if isinstance(self.model, pv.MultiBlock):
            print("Model is a MultiBlock object.")
            for i, part in enumerate(self.model):
                self.plotter.add_mesh(part, pickable=True)
        else:
            print("Model is not a s object.")
            self.plotter.add_mesh(self.model, pickable=True)
        print("Model parts:")

        self.plotter.disable_picking()
        self.plotter.enable_point_picking(callback=self._on_pick, use_picker=True, show_point=False)
        self.plotter.show(auto_close=False)

if __name__ == "__main__": 
    body_model = BodyModel("male.glb")
    body_model.run()

