import {Module} from "@nestjs/common";
import {TypeOrmModule} from "@nestjs/typeorm";
import {BusEntity} from "./bus.entity";
import {BusesController} from "./buses.controller";
import {BusesService} from "./buses.service";

@Module({
    imports:[TypeOrmModule.forFeature([BusEntity])],
    controllers:[BusesController],
    providers:[BusesService]
})
export class BusesModule{}
