<script setup>
  // src/components/Form.vue

  const submitHandler = async (fields) => {
    // Let's pretend this is an ajax request:
    await new Promise((r) => setTimeout(r, 1000))
    console.log(fields)
  }
</script>

<template>
  <FormKit type="form" @submit="submitHandler">
    <FormKit type="text" label="Name" name="name" />
    <FormKit type="email" label="Email" name="email" />
  </FormKit>
</template>
