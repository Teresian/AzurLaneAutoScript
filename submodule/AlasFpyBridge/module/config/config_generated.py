import datetime

# This file was automatically generated by module/config/config_updater.py.
# Don't modify it manually.


class GeneratedConfig:
    """
    Auto generated configuration
    """

    # Group `Scheduler`
    Scheduler_Enable = False
    Scheduler_NextRun = datetime.datetime(2023, 1, 1, 5, 0)
    Scheduler_Command = 'Fpy'
    Scheduler_SuccessInterval = 60
    Scheduler_FailureInterval = 120
    Scheduler_ServerUpdate = '05:00'

    # Group `Emulator`
    Emulator_ServerName = 'disabled'

    # Group `Error`
    Error_SaveError = False
    Error_OnePushConfig = 'provider: null'

    # Group `Optimization`
    Optimization_WhenTaskQueueEmpty = 'stay_there'

    # Group `FpyEmulator`
    FpyEmulator_Serial = '127.0.0.1:5555'
    FpyEmulator_Cmdline = 'python3 fgo.py cli --no-color'

    # Group `Interval`
    Interval_Interval = '07:00'

    # Group `Team`
    Team_Index = 0

    # Group `Apple`
    Apple_AppleKind = 'gold'  # gold, silver, bronze, copper, quartz
    Apple_AppleCount = 0
    Apple_EatOnce = True
    Apple_AppleTotal = 999

    # Group `Limit`
    Limit_Defeated = True
    Limit_KizunaReisou = True
    Limit_SpecialDrop = 0

    # Group `Benchmark`
    Benchmark_BenchTouch = True
    Benchmark_BenchScreen = True

    # Group `Call`
    Call_Function = 'lottery'  # fpSummon, lottery, mining, mail, synthesis, summonHistory

    # Group `Storage`
    Storage_Storage = {}
