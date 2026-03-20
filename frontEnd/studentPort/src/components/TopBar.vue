<script>
    export default{
        props: ["title"]
    }
</script>

<template>
    <div class="topbar">
        <h3>{{ title }}</h3>

        <div class="right">
            <span class="user">👤</span>
        </div>
    </div>
</template>

<style>
    .topbar{
        display:flex;
        justify-content:space-between;
        align-items:center;
        background:#e5e5e5;
        padding:10px 20px;
        border-radius:8px;
    }
</style>