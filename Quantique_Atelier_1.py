# Ce code génère un circuit quantique avec deux qubits sur un ordinateur quantique IBM Quantum.

# Imports
import os
from dotenv import load_dotenv
from qiskit import QuantumCircuit
from qiskit_ibm_runtime import QiskitRuntimeService, SamplerV2 as Sampler

# Charger les variables d'environnement
load_dotenv()

# Token
QiskitRuntimeService.save_account(
    token=os.getenv("IBM_QUANTUM_KEY"),
    channel="ibm_quantum"
)

# Création d'un circuit quantique simple
example_circuit = QuantumCircuit(2)
example_circuit.measure_all()

# Connexion à IBM Quantum
service = QiskitRuntimeService()
backend = service.least_busy(operational=True, simulator=False)

# Exécution
sampler = Sampler(backend)
job = sampler.run([example_circuit])

# Affichage des informations du job
print(f"Job ID: {job.job_id()}")

# Affichage des résultats
result = job.result()
print("Résultat du job:", result)
