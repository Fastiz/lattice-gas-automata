from FilesReader import FilesReader
from GasDrawer import GasDrawer


class SimulationRunner:

    def runMultipleSimulations(self, paths):
        for path in paths:
            reader = FilesReader(path)

            chunkSize, map, particles = reader.readStatic()

            drawer = GasDrawer(map, chunkSize, "N = " + str(particles))

            velocities, maxVel = reader.readNextTime()

            while len(velocities) > 0:
                drawer.update(velocities, maxVel)
                velocities, maxVel = reader.readNextTime()

    def runSingleSimulation(self, path):
        reader = FilesReader(path)

        chunkSize, map, particles = reader.readStatic()

        drawer = GasDrawer(map, chunkSize, "N = " + str(particles))

        velocities, maxVel = reader.readNextTime()

        while len(velocities) > 0:
            drawer.update(velocities, maxVel)
            velocities, maxVel = reader.readNextTime()
