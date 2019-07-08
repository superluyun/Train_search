<template>
    <div id="index">
        <div class="layui-form sel">
            <div class="layui-form-item">
                <select>
                    <option value="">请输入车站</option>
                    <option  v-for="item in stations" :value="item" :key="item">{{item}}</option>
                </select>
            </div>
            <router-link to="/result"><button type="button" class="layui-btn self_btn">查询</button></router-link>
        </div>
    </div>
</template>

<script>
    export default {
        name: "index",
        data(){
            return{
                stations:[],
            }
        },
        mounted(){
            this.$http.get("http://127.0.0.1:8000/api/stations").then(res=>{
                this.stations = res.body;
            })
        },
    }
    layui.use('form', function(){
        var form = layui.form;
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