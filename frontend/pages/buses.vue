<template>
  <container>
    <h2 v-if="buses.length>0">Загруженность автобусов</h2>
    <hr>
    <ul v-for="route in Object.keys(buses)" :key="route">
      <h5> Номер автобуса:{{ route }}</h5>
      <li v-for="bus in buses[route]" :key="bus">Айди автобуса:{{ bus.specificBusId }} . Количество людей:
        {{ bus.passengerAmount }} .
        Загруженность:{{ bus.passengerAmount < 30 ? "Низкая" : bus.passengerAmount < 50 ? "Средняя" : "Очень Высокая" }}
      </li>
      <hr>
    </ul>

  </container>
</template>

<script>

export default {
  name: 'BusesPage',
  async mounted() {
    let response = await fetch(window.location.origin + '/api/buses')
    response = await response.json()
    console.log(response)
    this.buses=response;
  },
  async data() {

    return {
      buses: []
    }
  }
}
</script>

<style scoped>

</style>
