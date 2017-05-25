import luigi
import inspect, os
import pandas as pd
import time


class BasePopulationLoad(luigi.Task):
    def requires(self):
        return None

    def output(self):
        return luigi.LocalTarget('population.csv')

    def run(self):
        time.sleep(15)


class InMigration(luigi.Task):
    def requires(self):
        return None

    def output(self):
        return luigi.LocalTarget('in_migration.csv')

    def run(self):
        time.sleep(15)


class OutMigrationRates(luigi.Task):
    def requires(self):
        return None

    def output(self):
        return luigi.LocalTarget('out_migration.csv')

    def run(self):
        time.sleep(15)


class BirthRates(luigi.Task):
    def requires(self):
        return None

    def output(self):
        return luigi.LocalTarget('births.csv')

    def run(self):
        time.sleep(15)


class DeathRates(luigi.Task):
    def requires(self):
        return None

    def output(self):
        return luigi.LocalTarget('deaths.csv')

    def run(self):
        time.sleep(15)


class NewPopulation(luigi.Task):
    def requires(self):
        return {'birth_rates': BirthRates(),
                'in_migration': InMigration()}

    def output(self):
        return luigi.LocalTarget('new_population.csv')

    def run(self):
        time.sleep(15)


class AgedPopulation(luigi.Task):
    def requires(self):
        return {'base_population': BasePopulationLoad(),
                'out_migration_rates': OutMigrationRates(),
                'death_rates': DeathRates()
                }

    def output(self):
        return luigi.LocalTarget('aged_population.csv')

    def run(self):
        time.sleep(15)


class FinalPopulation(luigi.Task):
    def requires(self):
        return {'aged_population': AgedPopulation(),
                'new_population': NewPopulation()
                }

    def output(self):
        return luigi.LocalTarget('final_population.csv')

    def run(self):
        time.sleep(15)


if __name__ == '__main__':
    luigi.run(main_task_cls=FinalPopulation)