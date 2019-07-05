<template>
    <div id="main">
        <div id="table">
            <table id="train_table" class="layui-table" lay-even>
                <colgroup>
                    <col width="40">
                    <col width="80">
                    <col width="80">
                    <col width="80">
                    <col width="80">
                </colgroup>
                <thead>
                    <tr>
                        <th lay-data="{field:'id'}">车次</th>
                        <th lay-data="{field:'username'}">始发站</th>
                        <th lay-data="{field:'sex'}">始发时间</th>
                        <th lay-data="{field:'city'}">终到站</th>
                        <th lay-data="{field:'sign'">到达时间</th>
                    </tr>
                </thead>
            </table>
        </div>
        <a href="/"><button type="button" class="layui-btn self_btn2">返 回</button></a>
    </div>
</template>

<script>
    export default {
        name: "result"
    }
    layui.use('table', function(){
        var table = layui.table;
        //第一个实例
    });
</script>

<style scoped>
    #main{
        width: 350px;
        margin-left: 5px;
    }
    #table{
        height: 460px;
    }
    .layui-table td, .layui-table th  {
        padding: 0;
        text-align: center;
    }
    .layui-table th{
        font-weight: bold;
    }
    .self_btn2{
        width: 100%;
    }
</style>