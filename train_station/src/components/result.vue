<template>
    <div id="main">
        <div id="table">
            <table id="train_table" :lay-data="url" class="layui-table" lay-even>
                <colgroup>
                    <col width="40">
                    <col width="80">
                    <col width="80">
                    <col width="80">
                    <col width="80">
                </colgroup>
                <thead>
                    <tr>
                        <th lay-data="{field:'station_train_code'}">车次</th>
                        <th lay-data="{field:'start_station_name'}">始发站</th>
                        <th lay-data="{field:'start_start_time'}">始发时间</th>
                        <th lay-data="{field:'end_station_name'}">终到站</th>
<!--                        <th lay-data="{field:'end_arrive_time'">到达时间</th>-->
                    </tr>
                </thead>
            </table>
        </div>
        <a href="/"><button type="button" class="layui-btn self_btn2">返 回</button></a>
    </div>
</template>

<script>
    export default {
        name: "result",
        mounted(){

        },
        data(){
            return{
                url:'http://127.0.0.1:8000/api/city?city='+this.city,
                city:""
            }
        }
    }
    layui.use('table', function(){
        // var table = layui.table;
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