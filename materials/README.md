# 演练资料格式

值班平台与告警源均为本地合成记录。分钟是同一演练时钟。影响范围以服务、地域、业务流组合标识。班表窗口为左闭右开。

## `topology` 调用范围及启用时刻

service 到 dependency 的有向调用，region 和 flow 限定影响范围。active_from_min 含端点，active_to_min 不含端点。没有在这一时刻生效的边时，该边不能用于推断覆盖。

字段为 `service`、`dependency`、`region`、`flow`、`active_from_min`、`active_to_min`。

## `ownership` 班表和各严重等级响应目标

ack_within_min 是从呼叫责任生效到需要确认的最长分钟。backup 在超时后需要接手，仍处在同一服务责任线上。 普通下游影响连续超过 normal_independent_min 分钟后需要独立处置。

字段为 `service`、`start_min`、`end_min`、`primary`、`backup`、`urgent_ack_min`、`normal_ack_min`、`normal_independent_min`。

## `alerts` 探针故障和恢复事实

occurred_min 为探针时间，observed_min 为进入值班平台时间。kind 有 fail、recover、independent。severity 只表示对此范围的紧急程度。evidence 为来源标识。

字段为 `observed_min`、`occurred_min`、`service`、`region`、`flow`、`kind`、`severity`、`evidence`。

## `pager` 消息平台和人员回执样例

delivery 行表示通知平台回执，ack 表示该人对该 scope 的确认。reference 是呼叫时传递的外部关联号。相同关联号的重复回执属于同一次通知。样例可由本地呼叫操作关联后投递。

字段为 `observed_min`、`kind`、`reference`、`actor`、`scope`、`outcome`。
