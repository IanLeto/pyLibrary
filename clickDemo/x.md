<table>
    <tr>
        <th colspan="4">名称</th>
        <th colspan="4">类型</th>
        <th colspan="4">描述</th>
    </tr>
    <tr>
        <th colspan="4">state</th>
        <th colspan="4">str</th>
        <th colspan="4">状态</th>
    </tr>
    <tr>
        <th colspan="4">region_ids</th>
        <th colspan="4">arr</th>
        <th colspan="4">发布地域</th>
    </tr>
    <tr>
        <th colspan="4">plan_id</th>
        <th colspan="4">int</th>
        <th colspan="4">计划id</th>
    </tr>
    <tr>
        <th colspan="4">plan_name</th>
        <th colspan="4">str</th>
        <th colspan="4">计划名称</th>
    </tr>
    <tr>
        <th colspan="4">isSql</th>
        <th colspan="4">bool</th>
        <th colspan="4">是否有sql审查（讨论）</th>
    </tr>
      <tr>
        <th colspan="4">product_id</th>
        <th colspan="4">int</th>
        <th colspan="4">产品</th>
    </tr>
      <tr>
        <th colspan="4">product_name</th>
        <th colspan="4">str</th>
        <th colspan="4">产品名</th>
    </tr>
    <tr>
        <th rowspan="14">sub_job<br>子任务组根据产品管理模块自动生成</th>
        <th colspan="2">sub_job_id</th>
        <th colspan="2">int</th>
        <th colspan="4">子任务id</th>
    </tr>
    <tr>
        <th colspan="2">sub_job_state</th>
        <th colspan="2">str</th>
        <th colspan="4">子任务状态</th>
    </tr>
    <tr>
        <th colspan="2">sub_job_type</th>
        <th colspan="2">str</th>
        <th colspan="4">子任务类型</th>
    </tr>
    <tr>
        <th colspan="2">sub_job_reigon（讨论）</th>
        <th colspan="2">str</th>
        <th colspan="4">子任务地域</th>
    </tr>
    <tr>
        <th colspan="2">sub_job_state</th>
        <th colspan="2">str</th>
        <th colspan="4">子任务状态</th>
    </tr>    
    <tr>
        <th colspan="2">module_id（topo结构讨论）<br> 一个子任务对应一个模块</br></th>
        <th colspan="2">int</th>
        <th colspan="4">模块id</th>
    </tr>
    <tr>
        <th colspan="2">module_name</th>
        <th colspan="2">str</th>
        <th colspan="4">模块名称</th>
    </tr>
    <tr>
        <th colspan="2">rank</th>
        <th colspan="2">str</th>
        <th colspan="4">子任务优先级</th>
    </tr>    
    <tr>
        <th colspan="2">sub_job_state</th>
        <th colspan="2">str</th>
        <th colspan="4">子任务状态</th>
    </tr>    
    <tr>
        <th colspan="2">pre_action_id(对内)</th>
        <th colspan="2">int</th>
        <th colspan="4">action_id</th>
    </tr>    
    <tr>
        <th colspan="2">pre_aciton_name</th>
        <th colspan="2">str</th>
        <th colspan="4">pre动作</th>
    </tr>    
    <tr>
        <th colspan="2">rollback_action</th>
        <th colspan="2">str</th>
        <th colspan="4">会滚动作</th>
    </tr>    
    <tr>
        <th colspan="2">target 讨论</th>
        <th colspan="2">str</th>
        <th colspan="4">target （讨论）</th>
    </tr>
    <tr>
        <th colspan="2">log（对内）</th>
        <th colspan="2">str</th>
        <th colspan="4">日志</th>
    </tr>
</table>