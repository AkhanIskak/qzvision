import {Body, Controller, Get, Post} from "@nestjs/common";
import {BusesService} from "./buses.service";

@Controller('/buses')
export class BusesController {
    constructor(private busServ: BusesService
    ) {
    }

    @Get()
    listBuses() {
        return this.busServ.listBuses();
    }

    @Post('/update')
    updateBus(@Body() body) {
        return this.busServ.updateBus(body);
    }
}
