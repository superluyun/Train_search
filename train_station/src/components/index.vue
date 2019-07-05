<template>
    <div id="index">
        <div class="layui-form sel">
            <div class="layui-form-item">
                <select name="interest" lay-filter="aihao" lay-search>
                    <option value="">请输入车站</option>
                    <option :value=i v-for="i in 30">{{i}}</option>
                </select>
            </div>
            <router-link to="/result"><button type="button" class="layui-btn self_btn">查询</button></router-link>
        </div>
    </div>
</template>

<script>
    export default {
        name: "index"
    }
    layui.use('form', function(){
        var form = layui.form;

        //各种基于事件的操作，下面会有进一步介绍
    });
</script>

<style>
    #index{
        margin-top: 60px;
    }
    .sel{
        width: 350px;
        margin-left: 5px;
    }
    .layui-edge{
        display: none;
    }
    .self_btn{
        margin-top: 20px;
        width: 100%;
    }
</style>