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


class OutMigration(luigi.Task):
    def requires(self):
        return None

    def output(self):
        return luigi.LocalTarget('out_migration.csv')

    def run(self):
        time.sleep(15)


class MigrationRates(luigi.Task):

    def requires(self):
        return {'in_migration': InMigration(),
                'out_migration': OutMigration()}

    def output(self):
        return luigi.LocalTarget('migration.csv')

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


class SurvivedPop(luigi.Task):
    def requires(self):
        return {'birth_rates': BirthRates(),
                'death_rates': DeathRates()}

    def output(self):
        return luigi.LocalTarget('deaths.csv')

    def run(self):
        time.sleep(15)


class AgedPopulation(luigi.Task):
    def requires(self):
        return {'base_population': BasePopulationLoad(),
                'out_migration': OutMigration(),
                'survived_pop': SurvivedPop()
                }

    def output(self):
        return luigi.LocalTarget('final_population.csv')

    def run(self):
        time.sleep(15)


class FinalPopulation(luigi.Task):
    def requires(self):
        return {'in_migration': InMigration(),
                'aged_population': AgedPopulation()
                }

    def output(self):
        return luigi.LocalTarget('final_population.csv')

    def run(self):
        time.sleep(15)


if __name__ == '__main__':
    luigi.run(main_task_cls=FinalPopulation)