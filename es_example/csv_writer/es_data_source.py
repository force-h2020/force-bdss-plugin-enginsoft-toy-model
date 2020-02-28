import math

from force_bdss.api import BaseDataSource, DataValue, Slot


class ESDataSource(BaseDataSource):
    """Defines an example data source.
    This data source specifically performs a power operation
    on its input.
    """

    def run_simulation(self, model, parameters):
        #rw_in = FileReaderWriter("./data.txt")
        #print(rw.getData())
        #print(parameters)
        #d = rw_in.getData()
        #XX = d["force.X"]
        #YY = d["force.Y"]
        XX = parameters["force.X"]
        YY = parameters["force.Y"]

        d_out = {}
        #if ( parameters[0]:
        #    model.X = parameters[0].value
        #    result = 1
        #elif ( parameters[0].type == 'type_heigth'):
        #    model.Y = parameters[0].value
        #rw_out = FileReaderWriter("./data_out.txt")
        
        B = math.pi * math.pow(XX, 2)
        d_out["force.B"] = B
        s = math.sqrt( math.pow(XX,2) + math.pow(YY,2))
        S = math.pi * XX * s
        d_out["force.S"] = S
        T = B + S
        d_out["force.T"] = T
        V = ( math.pow(XX,2) * YY * math.pi) / 3
        d_out["force.V"] = V
        #rw_out.writeData(d_out)
        #result = XX + YY
        result = d_out
        
        return result
    
    #: This is where your computation happens.
    #: You receive the model, and a list of parameters
    #: that come from the MCO.
    #: Parameters are not plain numbers, but are instead instances
    #: of the DataValue class. This method must return a list
    #: of DataValue instances, whose number must match the number of
    #: output slots.
    def run(self, model, parameters):
        d = parameters[0].value
        print("d =")
        print(d)
        values = [p.value for p in parameters]
        print('values=')
        print(values)
        value_types = [p.type for p in parameters]
        print('value_types=')
        print(value_types)
        #result = self.run_simulation(model, parameters)
        result = self.run_simulation(model, d)
        return [
            DataValue(
                type=model.cuba_type_out,
                value=result
            )]

    #: If a data source is a function, the slots are the number of arguments
    #: it takes as input, and the number of entities it returns as output.
    #: This method must return a tuple of tuples. (input_tuple, output_tuple)
    #: Each tuple contains Slot instances. You can decide this information
    #: according to the model content, therefore if your data source returns
    #: different data depending on its settings, you can definitely handle
    #: this case.
    #: In this case, the data source is like a function
    #:
    #:                    a = pow(b)
    #:
    #: so it has one input slot and one output slot.
    #: a function like
    #:
    #:                a, b = func(m,n,o)
    #:
    #: has three input slots and two output slots.
    def slots(self, model):
        return (
            (
                Slot(type=model.cuba_type_in),
            ),
            (
                Slot(type=model.cuba_type_out),
            )
        )
