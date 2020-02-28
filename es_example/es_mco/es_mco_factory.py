from force_bdss.api import BaseMCOFactory

from .es_mco_communicator import ESMCOCommunicator
from .es_mco_model import ESMCOModel
from .es_mco import ESMCO
from .parameters import RangedMCOParameterFactory


class ESMCOFactory(BaseMCOFactory):
    """An MCO factory is responsible for creating the objects
    relative to the MCOs.

    An MCO execution model is assumed to be as in Dakota.
    Dakota works as follows: it reads an input file containing the details of
    what to be carried out.
    specifically, it contains which parameters it is supposed to generate,
    which KPIs are obtained, and where is (path) the external program
    performing the transformation between a selection of the parameters
    and the resulting KPIs.

    This execution model is required for our system. Any other MCO that needs
    to be integrated in our system must support it.

    For the above reasons, the following classes are required:

    - A MCO, which is the core orchestrator of spawning the initial
      MCO executable, parsing its output and emitting events as the
      calculation progresses.
    - a MCO Model, which contains general configuration options of the MCO.
    - a set of MCO parameters that the MCO supports, which are specifications
      of which parameters the MCO should generate, according to some
      constraints.
    - A communicator, that is responsible to format the data in transit
      between the MCO executable (e.g. the dakota program) and the executable
      it spawns to compute a single evaluation.
    - and finally a Factory (this class) that is responsible for generating
      all of the above.
      
    Una fabbrica MCO è responsabile della creazione degli oggetti
    rispetto agli MCO.

    Si presume che un modello di esecuzione MCO sia come in Dakota.
    Dakota funziona come segue: legge un file di input contenente i dettagli di
    cosa fare.
    in particolare, contiene quali parametri dovrebbe generare,
    quali KPI vengono ottenuti e dove si trova (percorso) il programma esterno
    eseguendo la trasformazione tra una selezione dei parametri
    e i KPI risultanti.

    Questo modello di esecuzione è richiesto per il nostro sistema. Qualsiasi altro MCO di cui abbia bisogno
    per essere integrato nel nostro sistema deve supportarlo.

    Per i motivi sopra indicati, sono richieste le seguenti classi:

    - Un MCO, che è l'orchestratore principale della generazione dell'iniziale
      Eseguibile MCO, analizzando il suo output ed emettendo eventi come
      il calcolo avanza.
    - un modello MCO, che contiene opzioni di configurazione generali dell'MCO.
    - una serie di parametri MCO supportati dall'MCO, che sono specifiche
      di quali parametri l'MCO dovrebbe generare, secondo alcuni
      vincoli.
    - Un comunicatore, che è responsabile della formattazione dei dati in transito
      tra l'eseguibile MCO (ad esempio il programma dakota) e l'eseguibile
      si genera per calcolare una singola valutazione.
    - e infine una fabbrica (questa classe) che è responsabile della generazione
      tutti i precedenti.
    """
    #: See notes on Data Source Factory for everything not described.
    def get_identifier(self):
        return "es_mco"

    #: Returns a user visible name for the factory.
    def get_name(self):
        return "ES MCO"

    #: Returns the model class
    def get_model_class(self):
        return ESMCOModel

    #: Returns the optimizer class
    def get_optimizer_class(self):
        return ESMCO

    #: Returns the communicator class
    def get_communicator_class(self):
        return ESMCOCommunicator

    #: This method must return a list of all the possible parameter factory
    #: classes. This depends on what kind of parameters the MCO supports.
    def get_parameter_factory_classes(self):
        return [
            RangedMCOParameterFactory
        ]
