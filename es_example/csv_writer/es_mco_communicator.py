import sys
from .FileReaderWriter import FileReaderWriter

from force_bdss.api import (
    BaseMCOCommunicator,
    DataValue)


class ESMCOCommunicator(BaseMCOCommunicator):
    """The communicator is responsible for handing the communication protocol
    between the MCO executable (for example, the dakota executable) and the
    single point evaluation (our BDSS in --evaluate mode).

    This MCO communicator assumes that the communication happens via stdin
    and stdout, which is what dakota does when invoking an external program
    to perform a single point evaluation.
    
    Il comunicatore è responsabile della consegna del protocollo di comunicazione
    tra l'eseguibile MCO (ad esempio, l'eseguibile dakota) e il file
    valutazione a punto singolo (il nostro BDSS in modalità --evaluate).

    Questo comunicatore MCO presuppone che la comunicazione avvenga tramite stdin
    e stdout, che è ciò che fa dakota quando si richiama un programma esterno
    per eseguire una valutazione a singolo punto.
    """
    def receive_from_mco(self, model):
        """Receives data from the MCO (e.g. dakota) by reading from
        standard input the sequence of numbers that are this execution's
        parameter values.

        You can use fancier communication systems here if your MCO supports
        them.
        """
        rw_in = FileReaderWriter("./data.txt")
        #print(rw.getData())
        #print(parameters)
        d = rw_in.getData()
        print("d =")
        print(d)
        #XX = d["force.X"]
        #YY = d["force.Y"]
        #data = sys.stdin.read()
        #values = list(map(float, data.split()))
        values = list(map(float, d.values()))
        print("values =")
        print(values)
        value_names = [p.name for p in model.parameters]
        print(value_names)
        value_types = [p.type for p in model.parameters]
        print(value_types)

        # The values must be given a type. The MCO may pass raw numbers
        # with no type information. You are free to use metadata your MCO may
        # provide, but it is not mandatory that this data is available. You
        # can also use the model specification itself.
        # In any case, you must return a list of DataValue objects.
        #return [
        #    DataValue(type=type_, name=name, value=value)
        #    for type_, name, value in zip(
        #        value_types, value_names, values)]
        return [
            DataValue(type=value_types[0], name=value_names[0], value=d)
            ]


    def send_to_mco(self, model, data_values):
        """This method does the reverse. Once the single point evaluation
        is completed, this method is used to send the data back to the MCO.
        We assume in this case it's done via stdout, but you can use whatever
        your MCO may support.

        You will receive a list of data values that are your KPIs as exiting
        from the evaluation pipeline.
        """
        data = " ".join([str(dv.value) for dv in data_values])
        sys.stdout.write(data)
        print("data_values = ")
        rw_out = FileReaderWriter("./data_out.txt")
        for dv in data_values:
            print(dv.value)
            rw_out.writeData(dv.value)
        
        
