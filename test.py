from statistic import main
import coverage

# 初始化coverage
cov = coverage.Coverage()
cov.start()

# 执行你的代码
main()

# 停止coverage
cov.stop()
cov.save()
cov.report()